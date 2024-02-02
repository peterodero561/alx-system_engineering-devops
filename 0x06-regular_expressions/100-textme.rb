#!/usr/bin/env ruby
# A script that checks a 10 numbers exactly

def extract(log_entry)
  # Define a regex pattern to extract relevant information
  pattern = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

  # Use the pattern to find matches in the log entry
  match = log_entry.match(pattern)

  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]

    # Remove any non-alphanumeric characters from sender and receiver
    sender.gsub!(/[^a-zA-Z0-9+]/, '')
    receiver.gsub!(/[^a-zA-Z0-9+]/, '')

    return "#{sender},#{receiver},#{flags}"
  else
    return "Invalid log entry format"
  end
end

# check commandline arguments

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <argument>"
else
  argument = ARGV[0]
  extract(argument)
end
