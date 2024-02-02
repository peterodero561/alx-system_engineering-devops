#!/usr/bin/env ruby
# A script that checks a 10 numbers exactly

def extract(arg)
  regex = /\[from:([^\]]*)\] \[to:([^\]]*)\] \[flags:([^\]]*)\]/
  match_data = arg.match(regex)
  sender = match_data[1]
  receiver = match_data[2]
  flags = match_data[3]
  puts "#{sender}, #{receiver}, #{flags}"
end

# check commandline arguments

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <argument>"
else
  argument = ARGV[0]
  extract(argument)
end
