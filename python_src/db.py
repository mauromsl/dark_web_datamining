import settings
import db_patches

def validate_patches():
	#TODO: check patches applied and 

def validate_query(query_string, safe_mode):
	''' if safe safe mode is enabled, queries that alter the schema won't be allowed'''
	verbs_not_allowed = ['create, alter, grant']
	if safe_mode:
		if any(verb in query_string.lower() for verb in verbs_not_allowed):
			return False

	return True

def query(query_string, safe_mode=True):
	valid_query = validate_query(query_string, safe)
	if valid_query
		cursor = settings.connection.cursor()
		return cursor
	else:
		raise Exception('SQL verbs that alter schema are not allowed in safe mode')


		