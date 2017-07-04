import React, { Component } from 'react'
import Layout from './components/Layout'
import CoursesCard from './components/CoursesCard'
import CoursesDescription from './components/CoursesDescription'
import CoursesLectureCards from './components/CoursesLectureCards'
import CoursesSectionList from './components/CoursesSectionList'
import { Course } from './utils/cmu_course'
import { searchTips } from './helpers'

var moment = require('moment');

class Courses extends Component {
  constructor(props) {
    super(props);
    this.state = {
      course: null,
      colors: {
        majorColor: 'purple lighten-1',
        textMajorColor: 'white-text',
        courseidColor: 'purple-text text-darken-4',
        titleColor: 'purple-text text-darken-3',
        textAccentColor: 'teal-text text-accent-2'
      }
    }
  }

  componentWillMount() {
    console.log(this.props.params)
    fetch(`https://api.cmucoursefind.xyz/course/v1/course/${this.props.match.params.courseid}/`)
      .then((response) => { return response.json() })
      .then((jsonResponse) => {
        if (jsonResponse.course) {
          this.setState({
            course: new Course(jsonResponse.course)
          })
        }
        // TODO: deal with the case when there's a server error
        // TODO: deal with 404's
      })
  }

  render() {
    console.log(this.state.course)
    return (
      <Layout
        navbarProps={{
          searchTips: searchTips
        }}
        mainContent={
          (this.state.course) ? (
            /* course loaded */
            <div>
              <div className="row">
                <div className="col s12 l9">
                  <CoursesCard
                    course={this.state.course}
                    colors={this.state.colors}
                  />
                </div>
              </div>
              <div className="container">
                <div className="section">
                  <h4 class="">Description</h4>
                  <br />
                  <CoursesDescription content={this.state.course.desc}/>
                </div>
                {this.state.course.lectures &&
                  <div className="section">
                    <h4 class="">Lectures</h4>
                    <br />
                    <CoursesLectureCards 
                      meetings={this.state.course.lectures}
                      colors={this.state.colors}
                    />
                  </div>
                }
                {this.state.course.sections &&
                  <div className="section">
                    <h4 class="">Sections</h4>
                    <br />
                    <CoursesSectionList 
                      meetings={this.state.course.sections}
                      colors={this.state.colors}
                    />
                  </div>
                }
                <div className="section">
                  <h4 class="">Ratings</h4>
                  <br />
                </div>
              </div>
            </div>
          ) : (
            null
          )
        }
        footerProps={{
          leftFooterText: this.state.course ? this.state.course.semester : '',
          rightFooterText: <span>Please <a className="teal-text text-accent-1" href="http://www.google.com/recaptcha/mailhide/d?k=01wipM4Cpr-h45UvtXdN2QKQ==&c=r0MIa1Nhtz6i9zAotzfExghYzS_a8HaYrmn_MGl-GBE=" target="_blank">send me feedbacks !</a><br/></span>
        }}
      />
    )
  }
}

export default Courses;