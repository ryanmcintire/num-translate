import axios from "axios";
import applyCaseMiddleware from "axios-case-converter";

const GET_PATH = "/num_to_english?number=";
const POST_PATH = "/num_to_english";

const CLIENT = applyCaseMiddleware(axios.create());

const handleError = () => ({status: "Error communicating with translation service", numToEnglish: null});

export default class NumberTranslationService {
    async get(number) {
        try {
            const {data} = await CLIENT.get(`${GET_PATH}${number}`);
            return data;
        } catch {
            return handleError();
        }

    }

    async post(number) {
        console.log('trying to post...');
        try {
            console.log('timing...');
            await new Promise(resolve => setTimeout(resolve, 5000));
            console.log('getting data');
            const {data} = await CLIENT.post(POST_PATH, {number});
            console.log('returning data...' + data);
            return data;
        } catch {
            console.log('in handle error...');
            const thingy = handleError();
            console.log("Thingy: " + thingy);
            console.log(thingy);
            return thingy;
        }

    }
}