# React App

This is a React application that uses the FullCalendar library to display timesheet data retrieved from the Clockify API. The application displays the timesheet data in various calendar views and provides features to edit, delete, and view timesheet entries. The application also includes the ability to resize and move events, as well as view detailed information about a selected event.

# Getting Started

1. Clone the repository to your local machine using `git clone`
2. Install the dependencies by running npm install.
3. Create a .env file in the root directory of the project and add your Clockify API key in the format `REACT_APP_CLOCKIFY_API_KEY=<your_api_key>`.
4. Start the application by running `npm start`.

# Dependencies

This application uses the following dependencies:

* React
* FullCalendar
* dayGridPlugin
* timeGridPlugin
* listPlugin
* interactionPlugin

# Components

`HandleEventResize`: A component that handles the resizing of events in the calendar.
`HandleEventDrop`: A component that handles the moving of events in the calendar.
`TimeSheetDetails`: A component that displays detailed information about a selected event.

# API

This application retrieves timesheet data from the Clockify API. The `fetchTimesheetEntries` function in the `App` component sends a GET request to the API and retrieves the data in JSON format. The data is then formatted into the FullCalendar event format and displayed in the calendar.

# Calendar Views
The FullCalendar library provides four calendar views:

* Day Grid Month View: Displays the events in a month grid.
* Time Grid Week View: Displays the events in a week grid.
* Time Grid Day View: Displays the events in a day grid.
* List Month View: Displays the events in a list format.

The header toolbar of the calendar allows users to switch between these views.

# Features

The application provides the following features:

* Add new timesheet entries by clicking on the desired date and entering the necessary information.
* Edit existing timesheet entries by dragging and dropping the event to a new time or resizing the event to a new duration.
* Delete existing timesheet entries by clicking on the event and selecting "Delete" from the dropdown menu.
* View detailed information about a selected timesheet entry by clicking on the event and selecting "Details" from the dropdown menu.
