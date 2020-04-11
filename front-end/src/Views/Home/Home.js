import React from 'react'
import Parallax from "../../components/Parallax/Parallax";
import Grid from "@material-ui/core/Grid";

import './Home.css'

import classNames from 'classnames'
import UserForm from "./Form/UserForm";
import Paper from "@material-ui/core/Paper";

const image = require('../../assets/iceberg-during-daytime-53389.jpg');


const Home = (props) => {
  return (
    <div>
      <Parallax image={image}>
        <Grid container spacing={3}>
          <Grid item xs={12} sm={12} md={6}>
            <h1 className='title'>What if you were on the RMS Titanic?</h1>
            <h3 className='description'>Do you think you'd survive? <br/> Answer a few questions, a machine learning
              algorithm will return
              the result, saying if you'd survive or not. Simple like that! :)</h3>
          </Grid>
        </Grid>
      </Parallax>
      <div className='mainRaised'>
        <div className='formContainer'>
          <div className='content'>
            <UserForm/>


          </div>
          <div className='footer'>Made by Iury Melo. You can check my <a href={'https://github.com/iurymelo/'}
                                                                         target="_blank">
            GitHub</a>, and contact me through <a href={'https://www.linkedin.com/in/iuryamerico/'} target="_blank"
          >Linkedin</a>! <br /> To see this project's source code, visit: <a
            href={'https://github.com/iurymelo/would-you-survive-titanic'} target="_blank">
            Would You Survive Titanic: GitHub repository</a>.
          </div>

        </div>
      </div>
    </div>

  )
};

export default Home;
