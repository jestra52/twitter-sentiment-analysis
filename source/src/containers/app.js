// @packages
import CssBaseline from '@material-ui/core/CssBaseline';
import React from 'react';

// @scripts
import MasterPageContainer from './master-page';

const AppContainer = () =>
    (
        <React.Fragment>
            <CssBaseline />
            <MasterPageContainer />
        </React.Fragment>
    );

export default AppContainer;
