import discord
from discord.ext import commands
import json

class Lg:

    conf = {}

    def __init__(self, client, config):
        self.client = client
        self.config = config

        global conf
        conf = config


    @commands.command(pass_context = True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages = True)
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def lg(self, ctx, arg: str = None):

        msg = ctx.message


        if arg == "setup":

            await ctx.send("SETUP !")

        else:
            return





def setup(client):
    client.add_cog(Lg(client, client.config))
