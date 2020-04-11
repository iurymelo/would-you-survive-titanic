import React from 'react';
import {makeStyles} from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import FormControlLabel from "@material-ui/core/FormControlLabel";
import Checkbox from "@material-ui/core/Checkbox";
import Button from "@material-ui/core/Button";
import api from "../../../axios";
import CircularProgress from "@material-ui/core/CircularProgress";

const cabin = [
  {
    value: 1,
    label: 'First Class',
  },
  {
    value: 2,
    label: 'Second Class',
  },
  {
    value: 3,
    label: 'Economic Class',
  }
];

const sex = [
  {
    value: 0,
    label: 'Male'
  },
  {
    value: 1,
    label: 'Female'
  }
];

const useStyles = makeStyles((theme) => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: '25ch',
    },
  },
  title: {
    font: '400 18px Roboto, sans-serif',
    fontSize: '20px',
    align: 'center',
    paddingBottom: '10px'
  },
  spinnerRoot: {
    display: 'flex',
    '& > * + *': {
      marginLeft: theme.spacing(2),
    },
  },
}));

export default function UserForm() {
  const classes = useStyles();

  const [info, setInfo] = React.useState({
    sex: null,
    age: null,
    sibsp: 0,
    pclass: null,
  });

  const [checked, setChecked] = React.useState(false);

  const [loading, setLoading] = React.useState(false);

  const handleChange = (event, id) => {
    const nameId = id;
    switch (nameId) {
      case "married":
        let count = info['sibsp'];
        if (event.target.checked) {
          count += 1;
          setChecked(true)
        } else {
          count -= 1;
          setChecked(false)
        }
        setInfo({
          ...info,
          sibsp: count
        });
        break;

      case 'age':
        const ageInt = parseInt(event.target.value)
        if (ageInt > -1 && ageInt < 99)
          setInfo({
            ...info,
            age: ageInt
          });
        break;

      case 'pclass':
        setInfo({
          ...info,
          pclass: parseInt(event.target.value)
        });
        break;

      case 'sibsp':
        let valueSp = 0;
        if (checked) {
          valueSp = 1;
        } else {
          valueSp = 0
        }
        const spInt = parseInt(event.target.value)

        setInfo({
          ...info,
          sibsp: spInt + valueSp
        });
        break;

      case 'sex':
        if(event.target.value > -1 && event.target.value < 2) {
          if(Number.isInteger(event.target.value)) {
            setInfo({
              ...info,
              sex: parseInt(event.target.value),
            })
          }
        }

      default:
        break;
    }

  };

  const checkValidity = () => {
    let valid = true;
    let err = [];
    if(!info['age']) {
      err.push('Age is required.');
      valid=false;
    }
    if(info['age'] < 0 || info['age'] > 120) {
      err.push('Age must be between 0 and 120.');
      valid = false;
    }
    if(!Number.isInteger(info['age'])){
      err.push('Age must be an integer.');
      valid = false;
    }
    if(!Number.isInteger(info['sibsp'])){
      err.push('Siblings must be an integer');
      valid = false;
    }
    if(info['sibsp'] < 0 || info['sibsp' > 12]) {
      err.push('Siblings must be between 0 and 12');
      valid = false
    }
    if(info['sex'] == null){
      err.push('Sex is required. =)')
      valid = false;
    }
    if(info['sex'] < 0 || info['sex'] > 1 || !Number.isInteger(info['sex'])){
      err.push('Sex invalid! This will be reported!')
      valid = false;
    }
    if(info['pclass'] < 0 || info['pclass'] > 3 || !Number.isInteger(info['pclass'])) {
      err.push('Cabin Class invalid! This will be reported!')
      valid = false;
    }

    return [valid, err]
  };

  const submitHandler = (event) => {
    event.preventDefault();
    const [valid, erroMsg] = checkValidity();
    if(valid){
      setLoading(true)
      api.request(`/predict?age=${info['age']}&sex=${info['sex']}&pclass=${info['pclass']}&sibsp=${info['sibsp']}`)
        .then(res => {
          setLoading(false);
          if(res.data.survived == 1) {
            alert('Wooow! You would survive! But why did you let Jack go?')
          } else {
            alert('Sorry Fish Food, you would die.')
          }
          window.location.reload()
        })
        .catch(err => {
          setLoading(false);
          console.log(err);
          window.location.reload()
        });
    }
    else {
      alert('Something is wrong! Error message(s):\n' + erroMsg.join('\n'))
    }
  };

  const spinner = (
    <div className={classes.root}>
      <CircularProgress />
    </div>
  );

  const form = (
    <form className={classes.root} noValidate autoComplete="off" onSubmit={submitHandler}>
      <div>
        <h1 className={classes.title}>Please, enter some information:</h1>
        <div style={{width: '600px', display: 'flex', justifyContent: 'center'}}>
          <TextField required id="standard-required"
                     label="Age"
                     onChange={(event) => handleChange(event, "age")}
          />

          <TextField
            id="sex"
            select
            label="Sex"
            helperText="XX or XY"
            onChange={(event) => handleChange(event, 'sex')}
          >
            {sex.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </TextField>
        </div>
        <div style={{width: '600px', display: 'flex', justifyContent: 'center'}}>
          <TextField id="standard-required"
                     label="How many siblings?"
                     onChange={(event) => handleChange(event, "sibsp")}
          />
          <TextField
            id="pclass"
            select
            label="Cabin Class"
            onChange={(event) => handleChange(event, "pclass")}
            helperText="What class do you usually travel?"
          >
            {cabin.map((option) => (
              <MenuItem key={option.value} value={option.value}>
                {option.label}
              </MenuItem>
            ))}
          </TextField>
        </div>
        <div style={{width: '600px', display: 'flex', justifyContent: 'center'}}>
          <FormControlLabel
            control={
              <Checkbox
                onChange={(event) => handleChange(event, 'married')}
                name="married"
                color="primary"
              />
            }
            label="Are you married?"
          />
        </div>
      </div>
      <div style={{width: '530px', display: 'flex', justifyContent: 'right'}}>
        <Button type={'submit'}>Submit</Button>
      </div>
    </form>
  );

  const page = loading ? spinner : form

  return (
    <div>
      {page}
    </div>
  );
}