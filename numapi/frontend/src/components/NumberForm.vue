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
          <div class="form-group spacer">
            <span class="spacer">
              <button class="btn btn-outline-primary" v-on:click="get">GET</button>
            </span>
            <span class="spacer">
              <button class="btn btn-outline-danger" data-bs-toggle="modal" v-on:click="post" :disabled="loading">
                <span v-show="!loading">POST</span>
                <span class="spinner-border spinner-border-sm text-danger" v-show="loading"></span>
              </button>
            </span>
          </div>
        </form>
        <div class="row">
          <div class="text-danger">
            {{ translationError }}
          </div>
          <div class="text-white">
            Translated number: {{ translatedNumber }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

const STATUS_OK = "ok";

export default {
  name: "NumberForm",
  inject: ["numberTranslationService"],
  methods: {
    async get(e) {
      e.preventDefault();
      this.clearOutput();
      this.updateDisplay(await this.numberTranslationService.get(this.number));
    },
    async post(e) {
      try {
        this.loading = true;
        e.preventDefault();
        this.clearOutput();
        const data = await this.numberTranslationService.post(this.number);
        this.updateDisplay(data);
        this.loading = false;
      } finally {
        this.loading = false;
      }

    },
    updateDisplay(data) {
      console.log('in update display: ' + data);
      const {status, numToEnglish} = data;
      this.translationError = status === STATUS_OK ? "" : status;
      this.translatedNumber = numToEnglish;
      this.number = "";
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
.spinner-spacing {

}

.spacer {
  padding: 20px 20px 20px 0;
}
</style>