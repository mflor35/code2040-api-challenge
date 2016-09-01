#! /bin/irb
require 'httparty' # Not part of ruby's STD library
require 'time'
class CODE2040

  @@base_url = "http://challenge.code2040.org/api/"
  def initialize(token='', github='')
    @token = token
    @github = github
    
  end

  def register(token, github)
    url = @@base_url + 'register'
    payload = {:token => @token, :github => @github}.to_json

    rsp = HTTParty.post(url,
                        :body => payload,
                        :headers => {'Content-Type' => 'application/json'})
    puts rsp
  end

  def challengeData(step, token=@token)
    url = @@base_url + step
    payload = {:token => token}.to_json
    rsp = HTTParty.post(url,
                        :body => payload,
                        :headers => {'Content-Type' => 'application/json'})
    return rsp
  end

  def validateSolution(step, token=@token, solution)
    puts "-- validating #{step} --"
    url = @@base_url + step + "/validate"
    payload = solution.merge!(token: token)
    puts "url = #{url}"
    puts "payload => #{payload}"
    rsp = HTTParty.post(url,
                        :body => payload,
                        :header => {'Content-Type' => 'application/json'})

    puts "response => #{rsp}"
  end

  def status
    url = @@base_url + "status"
    payload = {:token => @@token}.to_json
    rsp = HTTParty.post(url,
                        :body => payload,
                        :header => {'Content-Type' => 'application/json'})
    puts rsp
  end
  
end

def reverseString(string)
  puts
  puts "** Reversing the String **"
  reversed_str = string.reverse
  puts "#{string} => #{reversed_str}"
  return {:string => reversed_str}
end

def withoutPrefix(prefix, strings_array)
  puts
  puts "** Finding string without prefix **"
  puts "prefix => #{prefix}"
  puts "array => #{strings_array}"
  strings_array.delete_if{ |string| string.include?(prefix)}
  return {:array => strings_array}
end

def findNeedle(needle, haystack)
  puts
  puts "** Finding needle **"
  needle_index = haystack.index(needle)
  puts "Needle => #{needle_index}"
  return {:needle => needle_index}
end

def addToISO8601(datestamp, interval)
  puts
  puts "** Solving dating game **"
  puts "datestamp => #{datestamp}"
  puts "interval => #{interval}"
  
  date = Time.iso8601(datestamp)
  puts date
  new_date = date + interval.to_i
  return {:datestamp => new_date.iso8601.to_str}
  
end

api_challenge = CODE2040.new("174f74259da7236f9a2011c1c0b68511",
                             "https://github.com/mflor35/code2040-api-challenge")


string = api_challenge.challengeData(step='reverse')
reversed = reverseString(string)
api_challenge.validateSolution(step='reverse', solution=reversed)

needle_haystack = api_challenge.challengeData(step='haystack')
needle = findNeedle(needle_haystack["needle"], needle_haystack["haystack"])
api_challenge.validateSolution(step="haystack", solution=needle)

prefix_data = api_challenge.challengeData(step='prefix')
no_prefix = withoutPrefix(prefix_data["prefix"], prefix_data["array"])
api_challenge.validateSolution(step="prefix", solution=no_prefix)

datestamp = api_challenge.challengeData(step="dating")
new_datestamp = addToISO8601(datestamp["datestamp"], datestamp["interval"])
api_challenge.validateSolution(step="dating", solution=new_datestamp)
