#!/usr/bin/env ruby
# Regular expression that must match capital letters only
puts ARGV[0].scan(/[A-Z]/).join
