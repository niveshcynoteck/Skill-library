# Inbox Curator — Architecture Diagram

```mermaid
flowchart TB
    subgraph Celery["Celery (Redis broker on localhost:6380)"]
        BEAT["Celery Beat Scheduler"]
        WORKER["Celery Worker"]
        APP["src/app.py — entry point"]
    end

    subgraph Scheduler["Scheduler"]
        BS["BaseScheduler (ABC)
            Celery app · crontab · beat registration"]
        EC["EmailCurator
            fetch → batch → handler chain"]
        TR["TokenRefresh (Observer subject)
            refresh → notify observers"]
    end

    subgraph Pipeline["Email Pipeline"]
        F["EmailFetcher
            Graph API → normalize → Redis queue"]
        DC["DeleteHandler → BounceHandler → GroupHandler
            (Chain of Responsibility)"]
        REDIS[("Redis
            'emails' queue")]
    end

    subgraph External["External APIs"]
        GRAPH["Microsoft Graph API"]
        APIKEY["Backend APIs
            (filters, bounce, grouped)"]
    end

    APP --> TR
    APP --> EC
    TR -->|register_observer / update(token)| F
    TR -->|register_observer / update(token)| DC
    BEAT --> WORKER
    WORKER -->|email_processing| EC
    WORKER -->|token_refreshing| TR

    F -->|GET emails| GRAPH
    F -->|rpush json per email| REDIS
    EC -->|lrange/ltrim batches| REDIS
    EC --> DC
    DC -->|POST bounced / grouped| APIKEY
    DC -->|DELETE email| GRAPH
```

# Class / Inheritance Diagram

```mermaid
classDiagram
    class BaseScheduler {
        +Celery app
        -_instance
        +__new__(cls, *args, **kwargs)
        +__init__(*, task_name, schedule_time)
        +task()* 
        +create_crontab_schedule(**kwargs)
        +register_task()
    }

    class TokenRefresh {
        +observers: list
        +tokens: Tokens
        +register_observer(observer)
        +task()
        +task_refresh_tokens()
        +task_notify_observers()
    }

    class EmailCurator {
        +email_fetcher: EmailFetch
        +handler_chain: EmailHandler
        +task()
    }

    class EmailHandler {
        +next: EmailHandler
        +handle(email, context)
        +update(access_token)
        +response(payload, url)
    }

    class DeleteHandler {
        +handle(emails, context)
        +delete_email(email_id)
        +update(access_token)
    }

    class BounceHandler {
        +handle(emails, context)
        +extract_email_from_body(body)
    }

    class GroupHandler {
        +handle(emails, context)
        +keywordmatcher(text, keyword)
        +email_grouping(emails, groups)
    }

    class EmailFetch {
        +access_token: str
        +fetching_date: str
        +task()
        +task_fetch_and_store_emails()
        +update(access_token)
    }

    class Tokens {
        +access_token: str
        +refresh_token: str
        +get_tokens()
        +save_tokens()
    }

    BaseScheduler <|-- EmailCurator
    BaseScheduler <|-- TokenRefresh
    EmailHandler <|-- DeleteHandler
    EmailHandler <|-- BounceHandler
    EmailHandler <|-- GroupHandler
    EmailCurator --> EmailFetch
    EmailCurator --> DeleteHandler : handler chain head
    TokenRefresh --> Tokens
    TokenRefresh o-- "observers" EmailFetch
    TokenRefresh o-- "observers" DeleteHandler
```

# Email Processing Flow

```mermaid
sequenceDiagram
    participant Beat as Celery Beat
    participant Curator as EmailCurator.task()
    participant Fetcher as EmailFetcher
    participant Redis as Redis queue
    participant Chain as Delete→Bounce→Group
    participant API as Backend APIs

    Beat->>Curator: email_processing (09:30 daily)
    Curator->>Fetcher: task()
    Fetcher->>API: GET emails (Graph API, since yesterday)
    API-->>Fetcher: pages of emails
    loop per email
        Fetcher->>Redis: RPUSH emails (json per email)
    end
    Curator->>Redis: LLEN emails
    loop batches of 100
        Curator->>Redis: LRANGE 0..99 + LTRIM 99..-1
        Curator->>Chain: handle(emails, context)
        DeleteHandler->>API: DELETE Graph email
        BounceHandler->>API: POST bounced emails
        GroupHandler->>API: POST grouped emails
    end
```
