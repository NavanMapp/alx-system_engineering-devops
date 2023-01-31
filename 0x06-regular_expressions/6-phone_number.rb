#!/usr/bin/env ruby
# regular expression that must match 10 digits
puts ARGV[0].scan(/[0-9]{10}$/).join
