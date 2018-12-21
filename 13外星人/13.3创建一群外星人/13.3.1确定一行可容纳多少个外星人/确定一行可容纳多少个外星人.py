#屏幕宽度存储在ai_settings.screen_width中
#但需在屏幕两边都留下一定的边距，把它设置为外星人的宽度。
#由于有两个边距，因此可用于放置外星人的水平空间为屏幕宽度进去外星人宽度的两倍：
available_space_x = ai_settings.screen_width - (2 * alien_width)

#还需要在外星人之间留出一定的空间，即外星人宽度。
#因此显示一个外星人所需的水平空间为外星人宽度的两倍。
#一个宽度用于放置外星人，另一个宽度为外星人右边的空白区域。
#为确定一行空容纳多少个外星人，我们将可用空间除以外星人宽度的两倍
number_aliens_x = available_space_x / (2 * alien_width)

#我们将在创建外星人群时使用这些公式。