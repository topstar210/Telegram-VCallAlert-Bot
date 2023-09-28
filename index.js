import dotenv from 'dotenv';
import TelegramBot from 'node-telegram-bot-api';
import { Voice } from "@signalwire/realtime-api";

dotenv.config();

// replace the value below with the Telegram token you receive from @BotFather
const TgToken = process.env.TelegramToken;
const signalwire_project_id = process.env.signalwire_project_id;
const signalwire_api_token = process.env.signalwire_api_token;

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(TgToken, { polling: true });

const dateFormat = (date) => {
    const formattedDate = date.toLocaleString('en-US', {
        month: 'short',
        day: '2-digit',
        year: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        hour12: true,
        timeZoneName: 'short'
    });
    return `${formattedDate}`
}

const startBot = (bot, chatId) => {
    console.log(`bot working... chatId: ${chatId}`);

    const client = new Voice.Client({
        project: signalwire_project_id,
        token: signalwire_api_token,
        contexts: ["Fo-Prince", "Forward to Jeremy", "Forward to SAS center"],
    });

    client.on("call.received", async (call) => {
        console.log("Call received:", call.id, call.from, call.to);

        try {
            await call.answer();
            const formattedUTCDate = dateFormat(new Date());
            bot.sendMessage(chatId, ` new call :  ${ call.from } \n\n from : ${ call.to } \n\n on : ${ formattedUTCDate }`);

            console.log("Inbound call answered");
        } catch (error) {
            console.error("Error answering inbound call", error);
        }
    });

    bot.sendMessage(chatId, 'You will received this kind of message');
}

// Matches "/echo [whatever]"
bot.onText(/\/echo (.+)/, (msg, match) => {
    // 'msg' is the received Message from Telegram
    // 'match' is the result of executing the regexp above on the text content
    // of the message
    const chatId = msg.chat.id;
    const resp = match[1]; // the captured "whatever"

    if (resp == 'start') {
        startBot(bot, chatId);
    }
});

// Listen for any kind of message. There are different kinds of
// messages.
bot.on('message', (msg) => {
    const chatId = msg.chat.id;

    // send a message to the chat acknowledging receipt of their message
    const testTo = '+14255051343';
    const testFrom = '+14256581242';
    const formattedUTCDate = dateFormat(new Date());
    bot.sendMessage(chatId, ` It's a test. \n\n new call :  ${testTo} \n\n from : ${testFrom} \n\n on : ${formattedUTCDate}`);
});
