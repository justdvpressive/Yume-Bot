import discord
from discord.ext import commands
import json
from itertools import cycle
import asyncio


class Lg:

    conf = {}

    def __init__(self, client, config):
        self.client = client
        self.config = config

        global conf
        conf = config

    @commands.command(pass_context=True)
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    # @commands.cooldown(1, 20, commands.BucketType.user)
    async def lg(self, ctx, arg: str = None, iarg: int = None):

        msg = ctx.message
        guild = ctx.message.guild

        if arg == "setup":
            await ctx.send("SETUP...")
            global vchannel
            vchannel = await guild.create_voice_channel("Lg Register")
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(connect=False)
            }
            global gchannel
            gchannel = await guild.create_voice_channel("Game", overwrites=overwrites)
            # TODO: Faire un channel de jeux pour la narration et des salons invisibles pour chaques roles !
            return

        elif arg == "start":
            await ctx.send("Starting...")
            players = vchannel.members
            for player in players:
                await player.move_to(gchannel)
                await ctx.send("{} has joined the game".format(player.name))
                return

        elif arg == None:
            await ctx.send("Invalid arg")

        else:
            return


def setup(client):
    client.add_cog(Lg(client, client.config))
