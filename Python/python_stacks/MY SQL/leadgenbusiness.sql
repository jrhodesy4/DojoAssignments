-- 1. What query would you run to get the total revenue for March of 2012?

SELECT MONTHNAME(charged_datetime) as _month, SUM(amount) as revenue
	FROM billing
	WHERE MONTHNAME(charged_datetime) = 'March' AND YEAR(charged_datetime) = 2012;

-- 2. What query would you run to get total revenue collected from the client with an id of 2?

SELECT SUM(amount) as revenue
	FROM billing
	WHERE billing.client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?

SELECT sites.client_id, domain_name
	FROM sites
	WHERE sites.client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client=20?

SELECT sites.client_id, COUNT(sites.site_id) as num_sites, DATE_FORMAT(sites.created_datetime, '%M') AS month_created, DATE_FORMAT(sites.created_datetime, '%Y') AS year_created
	FROM sites
	WHERE sites.client_id = 1
	GROUP BY month_created, year_created;

-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?

SELECT sites.domain_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M %d, %Y') AS date_registered
	FROM sites
	LEFT JOIN leads
	ON sites.site_id = leads.site_id
	WHERE leads.registered_datetime
	BETWEEN '2011-01-01' AND '2011-02-15'
	GROUP BY sites.site_id;

-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS leads_counts
	FROM clients
	LEFT JOIN sites
    ON clients.client_id = sites.client_id
    JOIN leads
    ON sites.site_id = leads.site_id -- no left join here
	WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
	GROUP BY clients.client_id;

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS leads_count, DATE_FORMAT(leads.registered_datetime, '%M') AS 'month'
	FROM clients
	LEFT JOIN sites
    ON clients.client_id = sites.client_id
    JOIN leads
    ON sites.site_id = leads.site_id
	WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
	GROUP BY clients.client_id, MONTH(leads.registered_datetime)
	ORDER BY MONTH(leads.registered_datetime);

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.
-- Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS leads_count
	FROM clients
	JOIN sites
    ON clients.client_id = sites.client_id
    LEFT JOIN leads
	ON sites.site_id = leads.site_id
    WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
	GROUP BY clients.client_id, sites.domain_name;

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, sites.domain_name, COUNT(leads.leads_id) AS leads_count
	FROM clients
	JOIN sites
    ON clients.client_id = sites.client_id
    LEFT JOIN leads
	ON sites.site_id = leads.site_id
	GROUP BY clients.client_id, sites.domain_name;

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, SUM(billing.amount) AS revenue, DATE_FORMAT(billing.charged_datetime, '%M') AS 'month', DATE_FORMAT(billing.charged_datetime, '%Y') AS 'year'
	FROM clients
	LEFT JOIN billing
    ON clients.client_id = billing.client_id
	GROUP BY client_name, MONTH(billing.charged_datetime), YEAR(billing.charged_datetime)
	ORDER BY clients.client_id;

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that each row shows a new client.
-- It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, GROUP_CONCAT(sites.domain_name, ' / ') AS 'sites'
	FROM clients
	LEFT JOIN sites
    ON clients.client_id = sites.client_id
	GROUP BY clients.client_id;



