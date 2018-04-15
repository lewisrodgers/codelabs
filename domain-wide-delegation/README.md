# What setting up domain wide delegation might look like at an enterprise

At the enterprise level, there will be multiple teams or individuals responsible for different aspects of GCP and G Suite administration. Which means, there's a few moving parts when it comes to the setup of domain wide delegation for an application that needs it.

Here's what this might look like...

![complete]

## The Setup

For domain wide delegation (DwD) setup, we need to have 3 things:

1. A service account with DwD enabled
2. The json keyfile (client ID and secret) associated with the service account
3. And a list of API scopes

There'll be distinct roles responsible for providing and consuming each of these things that want to coordinate with each other. 

Let's say there are 3 roles: 

1. A developer from the development team
2. The GCP admin* from the operations team
3. And the G Suite domain admininstrator from some other part of IT

*GCP Admin is a generalized term I'm using to refer to someone who has the permissions to create service accounts, whether it be a GCP Project Owner or a Service Account Admin.

![roles]

## The Developer

In our scenario, the development team wants to build an application that accesses user data on the domain. They determine the APIs and list of API scopes to be used. What's missing is the json keyfile — or credentials — needed for authentication between the application and G Suite domain. 

![app-scopes]

## The GCP Admin

In order to get this, the development team asks the GCP Admin for a service account with DwD enabled. The GCP Admin chooses a service account and makes the json keyfile available to the developers.

![service-account-request]

## The G Suite Admin

The last step is to register the application with the G Suite domain. To do this, the G Suite Admin needs to know the client ID of the service account and API scopes the application will use. They'll add these values to the `Manage client API access` page of the G Suite console.

![gsuite-admin]

## Summary

Roles and responsibilities between organizations will differ, so it's important to understand the org structure, who is reponsible for what, how and where to make requests and get approvals.

### Resources
* [Using OAuth 2.0 for Server to Server Applications](https://developers.google.com/identity/protocols/OAuth2ServiceAccount)
* [Perform G Suite Domain-Wide Delegation of Authority](https://developers.google.com/admin-sdk/directory/v1/guides/delegation)
* [Perform Google Apps domain-wide delegation of authority](https://developers.google.com/+/domains/authentication/delegation)
* [OAuth: Managing API client access](https://support.google.com/a/answer/162106?hl=en)

[roles]: img/roles.png
[app-scopes]: img/app_scopes.png
[service-account-request]: img/service_account_request.png
[gsuite-admin]: img/gsuite_admin.png
[complete]: img/complete.png