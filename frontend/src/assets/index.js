/* eslint-disable unicorn/prefer-module */
// Centralized asset exports for the frontend (CommonJS)
// Converted to CommonJS to match the project's current ESLint/parser settings.

// Prefer vector brand assets when available
const logoSvg = require('../../../Design-Assets/brand/logo.svg');
const logoMono = require('../../../Design-Assets/brand/logo-monochrome.svg');
const logoReversed = require('../../../Design-Assets/brand/logo-reversed.svg');
const pngLogo = require('../../../Design-Assets/Tapin-Logo.png');
const wireframe = require('../../../Design-Assets/Wireframe.png');

const logo = logoSvg || pngLogo;

module.exports = { logo, logoSvg, logoMono, logoReversed, logoPng: pngLogo, wireframe };
