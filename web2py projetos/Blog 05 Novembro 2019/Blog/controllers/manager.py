
def index():
	grid=SQLFORM(db.post).process(next=(URL('../../default/index')))
	return dict(grid=grid)