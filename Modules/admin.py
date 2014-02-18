from BotKit import admin, command

@command('addadmin', True)
def parse(bot, channel, user, args):
    usr =args.split()[0]
    if admin().isadmin(usr):
        bot.msg(channel, "%s: %s is already an admin" % (user, usr))
    else:
        admin().add(usr)
        bot.msg(channel, "%s: I added %s to the admin group" % (user, usr))


@command('remadmin', True)
def parse(bot, channel, user, args):
    usr =args.split()[0]
    if usr.lower() == user.lower():
        bot.msg(channel, 'lol okay');

    if admin().isadmin(usr):
        admin().remove(usr)
        bot.msg(channel, "%s: I removed %s from the admin group" % (user, usr))
    else:
        bot.msg(channel, "%s: %s was never an admin" % (user, usr))
