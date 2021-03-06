import React, { Component } from 'react';

class CollapsibleElement extends Component {
  render() {
    return (
      <li>
        <div className="collapsible-header waves-effect hoverable">
          {/* TODO: class options */}
          <div className="row nomargin">
            <div className="col s12 m8 l8 truncate">
              {this.props.leftHeaderIcon}
              <span>
                {this.props.leftHeaderText}
              </span>
            </div>
            <div className="col m4 l4 hide-on-small-only">
              <span className="right badge">
                {this.props.rightHeaderText}
              </span>
            </div>
            <div className="col s12 hide-on-med-and-up">
              <span className="right grey-text text-darken-1">
                {this.props.rightHeaderTextShort}
              </span>
            </div>
          </div>
        </div>
        <div className="collapsible-body blue-grey darken-1">
          {this.props.bodyText}
        </div>
      </li>
    );
  }
}

export default CollapsibleElement;
