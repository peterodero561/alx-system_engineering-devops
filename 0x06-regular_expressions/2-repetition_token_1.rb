#!/usr/bin/env ruby
# A script that serch for  0 or 1 "b" in a pattern

def match(arg)
  regex = /hb{0,1}tn/
  matches = arg.scan(regex)
  result = matches.join
  puts result
end

#check for commandline arguments

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <argument>"
else
  args = ARGV[0]
  match(args)
end
