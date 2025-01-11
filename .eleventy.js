module.exports = function (eleventyConfig) {
    // Copy assets directory
    eleventyConfig.addPassthroughCopy("src/assets");

    return {
        dir: {
            input: "src",
            output: "_site",
            includes: "_includes"
        }
    };
};