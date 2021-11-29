require 'open-uri'
require 'zlib'
require 'yajl'

gz = open('http://data.gharchive.org/2021-11-25-15.json.gz')
js = Zlib::GzipReader.new(gz).read

Yajl::Parser.parse(js) do |event|
  print event
end