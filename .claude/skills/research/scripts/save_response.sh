#!/bin/bash

topic= "Topic"
mkdir "$topic"
cd "$topic"
if [ "$userResponse" = "yes" ]; then
	for i in "subtopics"; do
		touch "$i.md"
		# Write the corresponding section content to the file. 
		# Each file should contain only the content for that section.
	done
  touch "README.md" # To provide an overview of the topic and its subtopics and explain the file structure.
fi