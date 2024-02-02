#!/usr/bin/env ruby
# The regular expression must match School
# Using the project instructions, create a Ruby script that
# accepts one argument and pass it to a regular expression matching metho

def match_school(arg)
  regex = /School/
  if arg =~ regex
    puts "'#{arg}'"
  end
end

#check if atleat one command line argument is provided

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <argument>"
else
  argument = ARGV[0]
  match_school(argument)
end
