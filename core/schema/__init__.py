from ariadne import gql, make_executable_schema

from core.schema.queries import query
from core.schema.mutations import mutation

type_defs = gql("""
    type Query {
        hello: String!
        url(hash: String!): Url!
    }

    type Mutation {
        createUrl(url: String!): Url!
    }

    type Url {
        id: ID!
        url: String!
        hash: String!
    }
""")

schema = make_executable_schema(type_defs, query, mutation)
