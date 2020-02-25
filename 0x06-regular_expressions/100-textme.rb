#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(\+?\w+)\]\s\[to:(\+?\w+)\]\s\[flags:([-?[0-1]:?]+)\]/).join(",")
