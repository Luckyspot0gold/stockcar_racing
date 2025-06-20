# In main game loop
if time.time() % 3600 == 0:  # Every hour
    retry_pending_achievements()
