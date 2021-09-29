import {mount} from "@vue/test-utils";
import NumberForm from "../../src/components/NumberForm";

const CLICK = "click";

const ERR_STATUS = "An error occurred.";
const ERR_TRANS = null;
const ERR_RESP = {status: ERR_STATUS, numToTranslate: ERR_TRANS};
const ERR_UNKNOWN_MSG = "Unknown error.";

const STATUS_OK = "ok";
const TRANS_OK = "one-hundred twenty-three";
const GOOD_RESP = {status: STATUS_OK, numToEnglish: TRANS_OK};

const TRANSLATION_SELECTOR = "#translation-text";
const ERROR_SELECTOR = "#error-text";
const GET_SELECTOR = "#btn-get";
const POST_SELECTOR = "#btn-post";
const SPINNER_SELECTOR = ".spinner-border";


const numberTranslationService = {
    get: async () => {
    },
    post: async () => {
    }
}

const OPTIONS = {global: {provide: {numberTranslationService}}};

let component;

describe("NumberForm.vue", () => {
    beforeEach(() => component = mount(NumberForm, OPTIONS))

    it("displays translation when 'GET' button selected", async () => {
        numberTranslationService.get = async () => GOOD_RESP;
        await component.find(GET_SELECTOR).trigger(CLICK);
        const translationText = component.find(TRANSLATION_SELECTOR);
        const errorText = component.find(ERROR_SELECTOR);
        expect(errorText.isVisible()).toBe(false);
        expect(translationText.isVisible()).toBe(true);
        expect(translationText.html()).toContain(TRANS_OK);
    })

    it("displays error message when 'GET' returns error response", async () => {
        numberTranslationService.get = async () => ERR_RESP;
        await component.find(GET_SELECTOR).trigger(CLICK);
        const translationText = component.find(TRANSLATION_SELECTOR);
        const errorText = component.find(ERROR_SELECTOR);
        expect(errorText.isVisible()).toBe(true);
        expect(translationText.isVisible()).toBe(false);
        expect(errorText.html()).toContain(ERR_STATUS);
    })

    it("displays error message when 'GET' throws exception", async () => {
        numberTranslationService.get = async () => {throw "Flagrant Error"};
        await component.find(GET_SELECTOR).trigger(CLICK);
        const translationText = component.find(TRANSLATION_SELECTOR);
        const errorText = component.find(ERROR_SELECTOR);
        expect(errorText.isVisible()).toBe(true);
        expect(translationText.isVisible()).toBe(false);
        expect(errorText.html()).toContain(ERR_UNKNOWN_MSG);
    })

    it("displays translation when 'POST' button selected", async() => {
        numberTranslationService.post = async () => GOOD_RESP;
        await component.find(POST_SELECTOR).trigger(CLICK);
        const translationText = component.find(TRANSLATION_SELECTOR);
        const errorText = component.find(ERROR_SELECTOR);
        expect(errorText.isVisible()).toBe(false);
        expect(translationText.isVisible()).toBe(true);
        expect(translationText.html()).toContain(TRANS_OK);
        expectButtonEnabledAndSpinnerNotVisible(component);
    })

    it("displays error message when 'POST' returns error response", async () => {
        numberTranslationService.post = async () => ERR_RESP;
        await component.find(POST_SELECTOR).trigger(CLICK);
        const translationText = component.find(TRANSLATION_SELECTOR);
        const errorText = component.find(ERROR_SELECTOR);
        expect(errorText.isVisible()).toBe(true);
        expect(translationText.isVisible()).toBe(false);
        expect(errorText.html()).toContain(ERR_STATUS);
        expectButtonEnabledAndSpinnerNotVisible(component);
    })

    it("displays error message when 'POST' throws exception", async () => {
        numberTranslationService.post = async () => {throw "Flagrant error"};
        await component.find(POST_SELECTOR).trigger(CLICK);
        const translationText = component.find(TRANSLATION_SELECTOR);
        const errorText = component.find(ERROR_SELECTOR);
        expect(errorText.isVisible()).toBe(true);
        expect(translationText.isVisible()).toBe(false);
        expect(errorText.html()).toContain(ERR_UNKNOWN_MSG);
        expectButtonEnabledAndSpinnerNotVisible(component);
    })
})

const expectButtonEnabledAndSpinnerNotVisible = component => validateButton(component, false);

const validateButton = (component, expected) => {
    const button = component.find(POST_SELECTOR);
    const spinner = component.find(SPINNER_SELECTOR);
    expect(button.isDisabled()).toBe(expected);
    expect(spinner.isVisible()).toBe(expected);
};
