#######################
### Graph Constants ###
#######################

# user publications
publication_variables = """
{
  "id": "%s"
}
"""
publication_operation_name = 'UserProfileFollowingCollections'
publication_query = open('./constants/queries/publications.graphql').read()