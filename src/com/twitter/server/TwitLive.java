package com.twitter.server;

/** Class TwitLive
 * @version 1.0
 * @author Mayank Kandpal
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.URL;
import java.net.URLConnection;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class TwitLive extends HttpServlet{
	
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) 
	throws ServletException, IOException {
	
		// Response object
		PrintWriter out = resp.getWriter();
		String twitter_id = req.getParameter("twitter_id");	
		
		if(twitter_id != null){

				//URL pythonAPI = new URL("http://twitlive123.heroku.com/?q="+twitter_id);
		        URL pythonAPI = new URL(""+twitter_id);

		        URLConnection yc = pythonAPI.openConnection();

		        BufferedReader in = new BufferedReader(
		                                new InputStreamReader(
		                                yc.getInputStream()));
		        String inputLine;

		        while ((inputLine = in.readLine()) != null) 
		            out.println(inputLine);
		        in.close();
			}else{
				out.println("Please enter a twitter userid in the param");
			}
	}
}