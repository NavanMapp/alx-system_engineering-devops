#!/usr/bin/env ruby
# Expression that must match start of h and ends with n
puts ARGV[0].scan(/h.n/).join
