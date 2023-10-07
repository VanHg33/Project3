CREATE TABLE jobsearch (
    "employer_name" VARCHAR(50)  NOT NULL ,
    "job_publisher" VARCHAR(50)  NOT NULL ,
	"job_id" VARCHAR(50)
    "job_employment_type" VARCHAR(50)  NOT NULL ,
    "job_title" VARCHAR(50)  NOT NULL,
	"job_apply_link" VARCHAR(100), 
	"job_description" 
	"job_posted_at_timestamp"
	"job_posted_at_datetime_utc"
	"job_city"
	"job_state"
	"job_country"
	"job_latitude"
	"job_longitude"
	"job_offer_expiration_datetime_utc"
	"job_offer_expiration_timestamp"
	"job_required_skills"
	"bachelors_degree"
	"job_min_salary"
	"job_max_salary"
	"job_salary_currency"
	CONSTRAINT "employer_name" PRIMARY KEY ("job_id")
);