const express = require('express');
const { Client } = require('discord.js-selfbot-v13');
const fs = require('fs');

const app = express();
const port = 3000;

const config = JSON.parse(fs.readFileSync('../config.json', 'utf8'));
const botToken = config.token;

const client = new Client({
    checkUpdate: false,
});
client.login(botToken);

app.get('/guildid=:guildId', (req, res) => {
  const guildId = req.params.guildId;

  if (client.readyAt) {
    const guild = client.guilds.cache.get(guildId);

    if (guild) {
      const memberCount = guild.memberCount;
      res.json({ memberCount });
    } else {
      res.status(404).json({ error: 'Guild not found' });
    }
  } else {
    res.status(503).json({ error: 'Bot is not logged in yet' });
  }
});

app.listen(port, () => {
  console.log(`RuskyAPI is running on port ${port}`);
});
