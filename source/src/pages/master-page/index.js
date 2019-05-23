// @packages
import Button from '@material-ui/core/Button';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import CardHeader from '@material-ui/core/CardHeader';
import CardActions from '@material-ui/core/CardActions';
import Grid from '@material-ui/core/Grid';
import PropTypes from 'prop-types';
import React, { PureComponent } from 'react';
import TextField from '@material-ui/core/TextField';
import Typography from '@material-ui/core/Typography';
import LinearProgress from '@material-ui/core/LinearProgress';
import axios from 'axios';
import { withStyles } from '@material-ui/core/styles';

// @styles
import styles from './styles';

class MasterPage extends PureComponent {
    constructor(props) {
        super(props);

        this.state = {
            result: null,
            review: '',
            showLoadingIndicator: false
        };

        this.handleOnGetReviewSentiment = this.handleOnGetReviewSentiment.bind(this);
        this.handleOnFieldChange = this.handleOnFieldChange.bind(this);
    }

    handleOnFieldChange(evt) {
        const { name, value } = evt.target;

        this.setState({ [name]: value });
    }

    handleOnGetReviewSentiment() {
        const { review } = this.state;

        if (review && review !== '') {
            this.setState({ showLoadingIndicator: true });
            axios
                .get('http://127.0.0.1:5000/api/sentiment', {
                    params: { review }
                })
                .then((response) => {
                    this.setState({
                        result: response.data.sentiment,
                        showLoadingIndicator: false
                    });
                })
                .catch((error) => { console.log(error); });
        }
    }

    render() {
        const { classes } = this.props;

        const {
            result,
            review,
            showLoadingIndicator
        } = this.state;

        return (
            <Card className={classes.masterPage}>
                <CardHeader title="Send your review!" />
                <CardContent>
                    <Grid container>
                        <Grid item xs={6}>
                            <Typography className={classes.headerText} component="h1" variant="body2">
                                Our bot will tell whether it's a good movie or not
                            </Typography>
                            <TextField
                                className={classes.review}
                                id="review"
                                label="Review"
                                multiline
                                name="review"
                                onChange={this.handleOnFieldChange}
                                rows={4}
                                rowsMax="4"
                                value={review}
                                variant="outlined"
                            />
                        </Grid>
                        <Grid item xs={6} className={classes.botResponse}>
                            <Typography variant="h5" gutterBottom>
                                Bot response
                            </Typography>
                            <Typography variant="h3" gutterBottom>
                                {result && result !== '' && `This is a ${result}`}
                            </Typography>
                            {showLoadingIndicator && <LinearProgress className={classes.loadingIndicator} />}
                        </Grid>
                    </Grid>
                </CardContent>
                <CardActions>
                    <Button
                        className={classes.submitButton}
                        onClick={this.handleOnGetReviewSentiment}
                        color="primary"
                        variant="outlined"
                    >
                        Send review
                    </Button>
                </CardActions>
            </Card>
        );
    }
}

MasterPage.propTypes = {
    classes: PropTypes.object.isRequired
};

export default withStyles(styles)(MasterPage);
