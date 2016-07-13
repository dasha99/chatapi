import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'chatapi')

# Skip these if your db has no auth. But it really should.


people_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'age': {
        'type': 'integer',
    },
    'weight': {
        'type': 'integer',
    },
     'sex': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 7,
    },
     'martial_status': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
    },
    'height': {
        'type': 'integer',
    },
    # 'role' is a list, and can only contain values from 'allowed'.
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    # An embedded 'strongly-typed' dictionary.
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}
people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<username>'.
    'additional_lookup': {
        'url': 'regex("(?![%20])\w+")',
        'field': 'username'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': people_schema
}

booking_schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    'booking_type': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'booking_id': {
        'type': 'integer',
    },
    'from_loc': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'to_loc': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'from_time': {
        'type': 'datetime',
    },
    'to_time': {
        'type': 'datetime',
    },
}
booking = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'booking',

    # by default the standard item entry point is defined as
    # '/booking/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/booking/<username>'.
    'additional_lookup': {
        'url': 'regex("(?![%20])\w+")',
        'field': 'username'
    },

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': booking_schema
}
DOMAIN = {
    'people': people,
    'booking': booking,
}
