client.on('guildMemberAdd', member => {
  const channel = member.guild.channels.cache.find(ch => ch.name === 'welcome');
  if (!channel) return;
  
  channel.send(`Welcome ${member}, ID: ${member.id}`);
});
