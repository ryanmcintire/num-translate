import {createApp} from 'vue';
import App from "./App.vue";
import NumberTranslationService from "./services/number-translation-service";

import "bootstrap/dist/css/bootstrap.css";
import "./assets/styles.css";

createApp(App)
    .provide("numberTranslationService", new NumberTranslationService())
    .mount('#app');
