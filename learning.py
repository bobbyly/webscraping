import json
import requests
import time

schema = {
  "definitions": {}, 
  "$schema": "http://json-schema.org/draft-07/schema#", 
  "$id": "http://example.com/root.json", 
  "type": "object", 
  "title": "The Root Schema", 
  "description": "An explanation about the purpose of this instance.", 
  "required": [
    "checked", 
    "dimensions", 
    "id", 
    "name", 
    "price", 
    "tags"
  ], 
  "properties": {
    "checked": {
      "$id": "#/properties/checked", 
      "type": "boolean", 
      "title": "The Checked Schema", 
      "description": "An explanation about the purpose of this instance.", 
      ], 
    }, 
    "dimensions": {
      "$id": "#/properties/dimensions", 
      "type": "object", 
      "title": "The Dimensions Schema", 
      "description": "An explanation about the purpose of this instance.", 
      "required": [
        "width", 
        "height"
      ], 
      "properties": {
        "width": {
          "$id": "#/properties/dimensions/properties/width", 
          "type": "integer", 
          "title": "The Width Schema", 
          "description": "An explanation about the purpose of this instance.", 
          "default": 0, 
          "examples": [
            5
          ], 
        }, 
        "height": {
          "$id": "#/properties/dimensions/properties/height", 
          "type": "integer", 
          "title": "The Height Schema", 
          "description": "An explanation about the purpose of this instance.", 
          "default": 0, 
          "examples": [
            10
          ], 
        }
      }
    }, 
    "id": {
      "$id": "#/properties/id", 
      "type": "integer", 
      "title": "The Id Schema", 
      "description": "An explanation about the purpose of this instance.", 
      "default": 0, 
      "examples": [
        1
      ], 
    }, 
    "name": {
      "$id": "#/properties/name", 
      "type": "string", 
      "title": "The Name Schema", 
      "description": "An explanation about the purpose of this instance.", 
      "default": "", 
      "examples": [
        "A green door"
      ], 
      "pattern": "^(.*)$"
    }, 
    "price": {
      "$id": "#/properties/price", 
      "type": "number", 
      "title": "The Price Schema", 
      "description": "An explanation about the purpose of this instance.", 
      "default": 0.0, 
      "examples": [
        12.5
      ], 
    }, 
    "tags": {
      "$id": "#/properties/tags", 
      "type": "array", 
      "title": "The Tags Schema", 
      "description": "An explanation about the purpose of this instance.", 
      "items": {
        "$id": "#/properties/tags/items", 
        "type": "string", 
        "title": "The Items Schema", 
        "description": "An explanation about the purpose of this instance.", 
        "default": "", 
        "examples": [
          "home", 
          "green"
        ], 
        "pattern": "^(.*)$"
      }
    }
  }
}

url = 'www.priceline.com.au/ustorelocator/location/searchJson/'

data = requests.get(url)

data.json()
 
print(data.json())