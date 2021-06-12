import discord
import random
from random import randint
from discord.ext import commands

class Rolls(commands.Cog):
	def __init__(self, client):
		self.client = client
		
	@commands.command()
	async def r(self, ctx, dice='d20'):
		prefix = ['Managed to roll ',
				  'Landed on ',
				  'Rolled ']
		def grammar(roll):
			definite = 'an'
			anvalues = [8, 11, 18]
			if roll in anvalues:
				returnval = f'{definite} {roll}.'
			else:
				returnval = f'{definite[:1]} {roll}.'
			return returnval
		if '+' in dice:
			dice_die, dice_modifier = dice.split('+')
		elif '-' in dice:
			dice_die, dice_modiier = dice.split('-')
		else:
			dice_die = dice
			dice_modifier = 0
		if dice_die[0] != 'd':
			dice_coefficient, dice_value = dice_die.split('d')
		else:
			dice_coefficient = 1
			dice_value = dice_die[1:]
		await ctx.channel.send(f'{random.choice(prefix)}{grammar(randint(int(dice_modifier) + 1, int(dice_coefficient)*int(dice_value) + int(dice_modifier)))}')
		
def setup(client):
	client.add_cog(Rolls(client))
