<template>

  <div class="container">
    <div class="col-md-6 offset-md-3">
      <div class="row">
        <h3 class="text-white h3 mb-3">Number Form</h3>
      </div>
      <div class="row text-start">
        <form class="text-white">
          <div class="form-group">
            <label for="numberInput" class="text-white">Input number: </label>
            <input type="text" class="form-control" id="numberInput"
                   placeholder="Enter number to translate to English"
                   v-model="number"/>
          </div>

          <!--          Buttons here are candidates for separate component; elected to keep here for simplicity. -->
          <div class="form-group spacer">
            <span class="spacer">
              <button id="btn-get" class="btn btn-outline-primary" @click="get">GET</button>
            </span>
            <span class="spacer">
              <button id="btn-post" class="btn btn-outline-danger" data-bs-toggle="modal" @click="post"
                      :disabled="loading">
                <span v-show="!loading">POST</span>
                <span class="spinner-border spinner-border-sm text-danger" v-show="loading"></span>
              </button>
            </span>
          </div>
        </form>
        <div class="row">
          <div id="error-text" class="text-danger"
               v-show="translationError != null && translationError.length > 0">
            {{ translationError }}
          </div>
          <div id="translation-text" class="text-white"
               v-show="translatedNumber != null && translatedNumber.length > 0">
            Translated number: {{ translatedNumber }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

const STATUS_OK = "ok";
const STATUS_UNKNOWN_ERR = "Unknown error.";

export default {
  name: "NumberForm",
  inject: ["numberTranslationService"], // Not thrilled about the string literal here, but
                                        // don't yet know Vue best practices.
  methods: {
    async get(e) {
      try {
        e.preventDefault();
        this.clearOutput();
        this.updateDisplay(await this.numberTranslationService.get(this.number));
      } catch (e) {
        console.error(e);
        this.updateDisplay({status: STATUS_UNKNOWN_ERR});
      }
    },
    async post(e) {
      try {
        this.loading = true;
        e.preventDefault();
        this.clearOutput();
        const data = await this.numberTranslationService.post(this.number);
        this.updateDisplay(data);
        this.loading = false;
      } catch (e) {
        console.error(e);
        this.updateDisplay({status: STATUS_UNKNOWN_ERR});
      } finally {
        this.loading = false;
      }
    },
    updateDisplay(data) {
      const {status, numToEnglish} = data;
      this.translationError = status === STATUS_OK ? "" : status;
      this.translatedNumber = numToEnglish;
    },
    clearOutput() {
      this.translatedNumber = "";
      this.translationError = "";
    }
  },
  data() {
    return {
      number: "",
      translatedNumber: "",
      translationError: "",
      loading: false
    }
  }
}
</script>

<style>

.spacer {
  padding: 20px 20px 20px 0;
}
</style>