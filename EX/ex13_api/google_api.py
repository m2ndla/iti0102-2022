"""EX13 - API."""

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import googleapiclient.discovery
import re

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
data_range = "A1:B"


def get_links_from_spreadsheet(id: str, token_file_name: str) -> list:
    """
    Return a list of strings from the first column of a Google Spreadsheet with the given ID.

    Example input with https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M
        get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')

    Returns
        ['https://www.youtube.com/playlist?list=PLPszdKAlKCXUhU3r25SOFgBxwCEr-JHVS', ... and so on]
    """
    """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
    data_lst = []
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id,
                                    range=data_range).execute()
        values = result.get('values', [])
        if not values:
            return []
        for row in values:
            # Print column A.
            data_lst.append(row[0])
        return data_lst
    except HttpError as err:
        print(err)
        return []


"""EX13 - API Part 2."""


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.

    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    # -*- coding: utf-8 -*-

    # Sample Python code for youtube.playlistItems.list
    # See instructions for running these code samples locally:
    # https://developers.google.com/explorer-help/code-samples#python
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    link_list = []
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    link_id_pattern = r"(?<==).*"
    link_id = re.findall(link_id_pattern, link)[0]
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

    request = youtube.playlistItems().list(
        part="contentDetails",
        playlistId=link_id
    )
    response = request.execute()
    for video in response["items"]:
        video_id = video["contentDetails"]["videoId"]
        link_list.append("https://www.youtube.com/watch?v=" + video_id)
    print(response)
    page_token = False
    token_id = ""
    if "nextPageToken" in response:
        page_token = True
        token_id = response["nextPageToken"]
    while page_token:
        new_request = youtube.playlistItems().list(
            part="contentDetails",
            pageToken=token_id,
            playlistId=link_id
        )
        new_response = new_request.execute()
        if "nextPageToken" not in new_response:
            page_token = False
        else:
            token_id = new_response["nextPageToken"]
        for video in new_response["items"]:
            video_id = video["contentDetails"]["videoId"]
            link_list.append("https://www.youtube.com/watch?v=" + video_id)
        print(new_response)
    print(link_list)
    return link_list
