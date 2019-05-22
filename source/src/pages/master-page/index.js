// @packages
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import PropTypes from 'prop-types';
import React from 'react';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';

// @styles
import styles from './styles';

const MasterPage = ({ classes }) => (
    <div className={classes.masterPage}>
        <Card>
            <CardHeader title="Esto" />
            <CardContent>
                <Typography component="p" variant="body2">
                    MasterPage
                </Typography>
            </CardContent>
        </Card>
    </div>
);

MasterPage.propTypes = {
    classes: PropTypes.object.isRequired
};

export default withStyles(styles)(MasterPage);
