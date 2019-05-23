/**
 * Returns a reference to the first object with the specified
 * value of the ID or NAME attribute.
 * @param {string} elementId - String that specifies the ID value.
 * @return {HTMLElement}
 */
export const getElementById = elementId =>
    document.getElementById(elementId);
