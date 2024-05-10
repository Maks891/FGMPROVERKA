async def vidat_cmd(message):
            await register_users(message)
            name, balance, btc, bank = await getbalance(message)
            reply_user_name = message.reply_to_message.from_user.get_mention(as_html=True)
            win = ['🙂', '😋', '😄', '🤑', '😃']
            rwin = random.choice(win)
            perevod = int(msg.text.split()[1])
            reply_user_id = msg.reply_to_message.from_user.id
            perevod2 = '{:,}'.format(perevod)
            user_id = msg.from_user.id
            status = cursor.execute("SELECT status from users where user_id = ?",
                                         (message.from_user.id,)).fetchone()
            balance2 = cursor.execute("SELECT balance from users where user_id = ?",
                                      (message.reply_to_message.from_user.id,)).fetchone()
            balance2 = round(balance2[0])
            if user_status[0] == 'Rab':
                await message.reply(f'💵 Вы выдали {perevod2}$ игроку {reply_user_name} {rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            if user_status[0] == 'Admin':
                await message.reply(f'💵 Вы выдали {perevod2}$ игроку {reply_user_name} {rwin}',
                                    parse_mode='html')
                cursor.execute(f'UPDATE users SET balance = {balance2 + perevod} WHERE user_id = "{reply_user_id}"')
                connect.commit()
            elif user_status[0] == 'Player':
                await message.reply(
                    f'{user_name}, Доступ к данной команде ограничен. Для покупки администратора обратитесь к создателю 👨‍🦰',
                    parse_mode='html')
