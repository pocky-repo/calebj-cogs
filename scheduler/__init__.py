from .scheduler import scheduler

def setup(bot):
	bot.add_cog(scheduler(bot))
