#!/usr/bin/env ruby
# A script that checks a 10 numbers exactly

def match_word(arg)
  regex = /[A-Z]/
  matches = arg.scan(regex)
  result = matches.join
  puts result
end

# check commandline arguments

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <argument>"
else
  argument = ARGV[0]
  match_word(argument)
end
