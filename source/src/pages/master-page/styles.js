import globals from '../../styles/globals';

export default theme => (Object.assign({}, globals(theme), {
    botResponse: {
        textAlign: 'center'
    },
    headerText: {
        marginBottom: 25
    },
    loadingIndicator: {
        margin: 10
    },
    masterPage: {
        margin: 100
    },
    review: {
        width: '100%'
    },
    submitButton: {
        marginBottom: 5,
        marginLeft: 5
    }
}));
