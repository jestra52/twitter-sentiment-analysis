/**
 * Allowed field variants:
 *  - outlined
 *  - filled
 *  - standard
 */
export const DEFAULT_FIELD_VARIANT = 'standard';

/**
 * Common colors.
 */
export const colors = {
    BLACK: '#000',
    DARK_CYAN: '#00A582',
    LAVENDER: '#E2F2F1',
    LIGHT_SEA_GREEN: '#00CBA0',
    TEAL: '#009979',
    WHITE: '#fff'
};

/**
 * Common z-indexes.
 */
export const zIndex = {
    AUTO_COMPLETE: 3000,
    FOOTER: 1000,
    LOADING_PAGE: 4000,
    PROFILE_MENU: 2000,
    TOP_BAR: 1000
};

/**
 * Global classes.
 */
export default theme => ({
    gblLink: {
        '&:hover': {
            textDecoration: 'underline'
        },
        color: theme.palette.primary.main,
        textDecoration: 'none'
    }
});

/**
 * Common dimensions
 */
export const dimensions = {
    FOOTER_HEIGHT: 40,
    MAIN_MENU_WIDTH: 300,
    MAIN_MENU_WIDTH_COLLAPSED: 70,
    TOP_BAR_HEIGHT: 64
};
