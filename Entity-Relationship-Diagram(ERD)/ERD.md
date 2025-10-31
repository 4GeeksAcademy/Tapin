🫶 Tapin Volunteer Platform — Entity Relationship Diagram (ERD)

This Entity Relationship Diagram (ERD) defines the core data structure for the Tapin Volunteer Platform, illustrating how users, organizations, and volunteer opportunities interact within the system.

🧑 USERS

Fields

Field	Type	Description
id	INT (PK)	Unique user ID
email	VARCHAR	User email (unique)
password	VARCHAR	Hashed user password
name	VARCHAR	Full name
role	ENUM('volunteer', 'organization')	Defines user type
phone	VARCHAR	Contact number
location	VARCHAR	City or region
bio	TEXT	Short user bio
profile_picture	VARCHAR	Profile image URL
created_at	DATETIME	Timestamp of account creation
updated_at	DATETIME	Last updated timestamp

Relationships

One User can own one Organization (if role = organization)

One User can have many Signups, Reviews, and Saved Opportunities

🏢 ORGANIZATIONS

Fields

Field	Type	Description
id	INT (PK)	Unique organization ID
user_id	INT (FK → Users.id)	Owner of the organization
organization_name	VARCHAR	Official organization name
description	TEXT	Mission or overview
address	VARCHAR	Street address
latitude	DECIMAL	Geo coordinate
longitude	DECIMAL	Geo coordinate
website	VARCHAR	Organization website
verified	BOOLEAN	Admin verification status
rating	DECIMAL	Average review rating
created_at	DATETIME	Creation timestamp

Relationships

Each Organization belongs to one User

Each Organization has many Opportunities

🌍 OPPORTUNITIES

Fields

Field	Type	Description
id	INT (PK)	Unique opportunity ID
organization_id	INT (FK → Organizations.id)	Parent organization
title	VARCHAR	Opportunity title
description	TEXT	Detailed info about the event
category	VARCHAR	Category (e.g., “Environment”, “Education”)
location	VARCHAR	Address or meeting point
latitude	DECIMAL	Geo coordinate
longitude	DECIMAL	Geo coordinate
date	DATE	Event date
start_time	TIME	Start time
end_time	TIME	End time
capacity	INT	Max volunteers allowed
current_signups	INT	Number of volunteers signed up
requirements	TEXT	Requirements or conditions
skills_needed	TEXT	Desired skills
age_minimum	INT	Minimum age
status	ENUM('open','closed','cancelled')	Availability
created_at	DATETIME	Created timestamp
updated_at	DATETIME	Updated timestamp

Relationships

Each Opportunity belongs to one Organization

Each Opportunity has many Signups and Reviews

Each Opportunity can be saved by many Users

✍️ SIGNUPS

Fields

Field	Type	Description
id	INT (PK)	Signup record ID
user_id	INT (FK → Users.id)	Volunteer user
opportunity_id	INT (FK → Opportunities.id)	Selected opportunity
status	ENUM('pending','confirmed','cancelled','completed')	Signup status
signed_up_at	DATETIME	Time of signup
checked_in_at	DATETIME	Check-in timestamp

Relationships

Represents a many-to-many relationship between Users and Opportunities

⭐ REVIEWS

Fields

Field	Type	Description
id	INT (PK)	Review ID
user_id	INT (FK → Users.id)	Reviewer
opportunity_id	INT (FK → Opportunities.id)	Reviewed opportunity
rating	INT	Rating (1–5)
comment	TEXT	Feedback text
created_at	DATETIME	Review date

Relationships

Many Reviews belong to one User

Many Reviews belong to one Opportunity

💾 SAVED_OPPORTUNITIES

Fields

Field	Type	Description
id	INT (PK)	Save record ID
user_id	INT (FK → Users.id)	User who saved
opportunity_id	INT (FK → Opportunities.id)	Saved opportunity
saved_at	DATETIME	Timestamp of saving

Relationships

Represents a many-to-many relationship between Users and Opportunities

🔗 ERD Relationship Summary
USERS ──< ORGANIZATIONS
USERS ──< SIGNUPS >── OPPORTUNITIES
USERS ──< REVIEWS >── OPPORTUNITIES
USERS ──< SAVED_OPPORTUNITIES >── OPPORTUNITIES
ORGANIZATIONS ──< OPPORTUNITIES

🧩 Notes

This schema supports Flask ORM models (SQLAlchemy) and a MySQL database.

Designed for scalability, allowing volunteers, organizations, and opportunities to expand easily.

Acts as a blueprint for both backend API structure and frontend data flow.